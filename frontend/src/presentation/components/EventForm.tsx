import { useState } from "react";
import { EventApi } from "../../infrastructure/api/EventApi";
import { useNavigate } from "react-router-dom";

export const EventForm = () => {
    const [form, setForm] = useState({
        name: "",
        description: "",
        location: "",
        date: "",
        category_id: "",
    });
    const [image, setImage] = useState<File | null>(null);
    const navigate = useNavigate();

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        setForm({ ...form, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();

        const data = new FormData();
        Object.entries(form).forEach(([key, value]) => data.append(key, value));
        if (image) data.append("image", image);

        await EventApi.create(data);
        navigate("/");
    };

    return (
        <form onSubmit={handleSubmit}>
            <h2>Crear Evento</h2>
            <input type="text" name="name" placeholder="Nombre" onChange={handleChange} required />
            <textarea name="description" placeholder="Descripción" onChange={handleChange} required />
            <input type="text" name="location" placeholder="Lugar" onChange={handleChange} required />
            <input type="datetime-local" name="date" onChange={handleChange} required />
            <input type="text" name="category_id" placeholder="ID de categoría" onChange={handleChange} required />
            <input type="file" onChange={(e) => setImage(e.target.files?.[0] ?? null)} />
            <button type="submit">Guardar</button>
        </form>
    );
};
