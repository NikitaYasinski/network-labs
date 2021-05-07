import { API_ROUTE } from '@/constants';
import { ItemType } from '@/shared/types';

class RequestService {
  public static get = async (url: string) => {
    try {
      const response = await fetch(`${API_ROUTE}${url}/`);
      const data = await response.json();
      return data;
    } catch (error) {
      console.error(error.message);
      throw error;
    }
  }

  public static post: (url: string, body: any) => Promise<[number, ItemType]>
    = async (url, body) => {
      try {
        const response = await fetch(`${API_ROUTE}${url}/`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(body),
        });
        const item: ItemType = await response.json();
        return [response.status, item];
      } catch (error) {
        console.error(error.message);
        throw error;
      }
    }

  public static put: (url: string, body: any) => Promise<[number, ItemType]>
    = async (url: string, body: any) => {
      try {
        const response = await fetch(`${API_ROUTE}${url}/`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(body),
        });

        const item: ItemType = await response.json();

        return [response.status, item];
      } catch (error) {
        console.error(error.message);
        throw error;
      }
    }

  public static del = async (url: string) => {
    try {
      const response = await fetch(`${API_ROUTE}${url}/`, {
        method: 'DELETE',
      });

      return response.status;
    } catch (error) {
      console.error(error.message);
      throw error;
    }
  }
}

export default RequestService;
