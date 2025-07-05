import styled from "styled-components";
import { EventList } from "../components/EventList";
import { CalendarFilter } from "../components/CalendarFilter";

const Container = styled.div`
  max-width: 960px;
  margin: 2rem auto;
  padding: 0 1rem;
`;

export const Home = () => (
    <Container>
        <h1>Gestión de Eventos</h1>
        <CalendarFilter />
        <EventList />
    </Container>
);