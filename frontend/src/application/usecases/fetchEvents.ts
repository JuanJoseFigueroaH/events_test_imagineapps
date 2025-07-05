import { EventService } from "../../domain/services/EventService";

export const fetchEvents = async (service: EventService) => {
    return await service.getAll();
};
