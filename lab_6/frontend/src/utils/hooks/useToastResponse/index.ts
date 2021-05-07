import { useToasts } from 'react-toast-notifications';
import ResponseStatusService from '@/services/ResponseStatusService';
import { ResponseStatus } from '@/services/ResponseStatusService/types';

export const useToastResponse = () => {
  const { addToast } = useToasts();

  return ({ statusCode, customStatusObject }: { statusCode?: number; customStatusObject?: ResponseStatus }) => {
    if (statusCode) {
      const statusObject = ResponseStatusService.handleStatusCode(statusCode);
      addToast(statusObject.message, { appearance: statusObject.type });
    }

    if (customStatusObject) {
      addToast(customStatusObject.message, { appearance: customStatusObject.type });
    }
  };
};
