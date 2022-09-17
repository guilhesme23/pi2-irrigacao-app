import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import GraphBox from ".";


test('if graph box text is rendered', () => {
    render(
        <MemoryRouter>
            <GraphBox />
        </MemoryRouter>
    );

    expect(screen.getByText("Relatório dos sensores")).toBeInTheDocument();
    expect(screen.getByText("Umidade do solo (%)")).toBeInTheDocument();
    expect(screen.getByText("Umidade do ar (%)")).toBeInTheDocument();
    expect(screen.getByText("Temperatura do ar (°C)")).toBeInTheDocument();
    expect(screen.getByText("Temperatura do solo (°C)")).toBeInTheDocument();
})
