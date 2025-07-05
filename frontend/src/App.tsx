import { GlobalStyles } from "./presentation/styles/GlobalStyles";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Home } from "./presentation/pages/Home";
import { Create } from "./presentation/pages/Create";

function App() {
  return (
    <>
      <GlobalStyles />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/crear" element={<Create />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
