import { createGlobalStyle } from "styled-components";

export const GlobalStyles = createGlobalStyle`
  * {
    box-sizing: border-box;
    font-family: 'Segoe UI', sans-serif;
    margin: 0;
    padding: 0;
  }

  body {
    background-color: #f7f8fa;
    color: #222;
  }

  h1, h2, h3 {
    margin-bottom: 1rem;
    color: #333;
  }

  form {
    max-width: 600px;
    margin: 2rem auto;
    padding: 2rem;
    background: white;
    border-radius: 8px;
    box-shadow: 0 0 12px rgba(0,0,0,0.1);
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  input, textarea, select {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 6px;
    font-size: 1rem;
  }

  button {
    background-color: #0070f3;
    color: white;
    border: none;
    padding: 12px;
    border-radius: 6px;
    cursor: pointer;
    transition: background 0.3s;
  }

  button:hover {
    background-color: #005ad1;
  }

  ul {
    list-style: none;
    padding: 0;
  }

  li {
    background: white;
    margin-bottom: 1rem;
    padding: 1rem;
    border-radius: 6px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .calendar {
    max-width: 300px;
    margin: 0 auto 2rem auto;
  }
`;
