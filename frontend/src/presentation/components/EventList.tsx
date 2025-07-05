import { useEffect, useState } from "react";
import { Event } from "../../domain/models/Event";
import { EventApi } from "../../infrastructure/api/EventApi";

export const EventList = () => {
    const [events, setEvents] = useState<Event[]>([]);

    useEffect(() => {
        EventApi.getAll().then(setEvents);
    }, []);

    const handleDelete = async (id: string) => {
        await EventApi.delete(id);
        setEvents(events.filter((e) => e.id !== id));
    };

    return (
        <div>
            <h2>Eventos</h2>
            <ul>
                {events.map((event) => (
                    <li key={event.id}>
                        <strong>{event.name}</strong> – {event.date}
                        <button onClick={() => handleDelete(event.id)}>Eliminar</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};
