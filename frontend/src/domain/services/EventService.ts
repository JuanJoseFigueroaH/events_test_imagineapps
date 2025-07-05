import { Event } from "../models/Event";

export interface EventService {
    getAll(): Promise<Event[]>;
    create(data: FormData): Promise<Event>;
    delete(id: string): Promise<void>;
    filterByDate(date: string): Promise<Event[]>;
}
