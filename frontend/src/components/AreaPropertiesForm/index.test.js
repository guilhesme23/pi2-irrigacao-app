import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import AreaPropertiesForm from ".";

test('if area properties text is rendered', () => {
    render(
        <MemoryRouter>
            <AreaPropertiesForm />
        </MemoryRouter>
    );

    expect(screen.getByText("Grid Layout")).toBeInTheDocument();
    expect(screen.getByText("Largura (m)")).toBeInTheDocument();
    expect(screen.getByText("Comprimento (m)")).toBeInTheDocument();
    expect(screen.getByText("Posição da base")).toBeInTheDocument();
})

test('if area properties buttons are rendered', () => {
    render(
        <MemoryRouter>
            <AreaPropertiesForm />
        </MemoryRouter>
    )

    expect(screen.getByText("Calcular rota")).toBeInTheDocument();
    expect(screen.getByText("Iniciar rota")).toBeInTheDocument();
    expect(screen.getByText("Parar rota")).toBeInTheDocument();
})
