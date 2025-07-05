import axios from "axios";
import { Event } from "../../domain/models/Event";
import { EventService } from "../../domain/services/EventService";

const API = axios.create({
    baseURL: "http://localhost:8000",
    headers: {
        Authorization: `Bearer ${localStorage.getItem("token")}`,
    },
});

export const EventApi: EventService = {
    getAll: async () => {
        const res = await API.get<Event[]>("/events");
        return res.data;
    },
    create: async (data: FormData) => {
        const res = await API.post("/events", data, {
            headers: { "Content-Type": "multipart/form-data" },
        });
        return res.data;
    },
    delete: async (id: string) => {
        await API.delete(`/events/${id}`);
    },
    filterByDate: async (date: string) => {
        const res = await API.get(`/events/by-date?date=${date}`);
        return res.data;
    },
};
