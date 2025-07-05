import Calendar from "react-calendar";
import "react-calendar/dist/Calendar.css";
import { useState } from "react";
import { EventApi } from "../../infrastructure/api/EventApi";
import { Event } from "../../domain/models/Event";

export const CalendarFilter = () => {
    const [selectedDate, setSelectedDate] = useState<any>(null);
    const [filtered, setFiltered] = useState<Event[]>([]);

    const handleChange = async (value: any) => {
        if (value instanceof Date) {
            setSelectedDate(value);
            const iso = value.toISOString();
            const results = await EventApi.filterByDate(iso);
            setFiltered(results);
        }
    };

    return (
        <div>
            <h3>Filtrar por Fecha</h3>
            <Calendar onChange={handleChange} value={selectedDate} />
            <ul>
                {filtered.map((e) => (
                    <li key={e.id}>{e.name}</li>
                ))}
            </ul>
        </div>
    );
};
