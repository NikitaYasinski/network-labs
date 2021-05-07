import { ResponseStatus } from '@/services/ResponseStatusService/types';

class ResponseStatusService {
  public static handleStatusCode: (status: number) => ResponseStatus
  = (status: number) => {
    switch (status) {
      case 200:
        return { type: 'success', message: 'Created' };
      case 201:
        return { type: 'success', message: 'Success' };
      case 204:
        return { type: 'success', message: 'Success' };
      case 404:
        return { type: 'error', message: 'Error 404: Not found' };
      case 400:
        return { type: 'error', message: 'Error 400: Bad request' };
      default:
        return { type: 'warning', message: 'Unknown status code' };
    }
  }
}

export default ResponseStatusService;
