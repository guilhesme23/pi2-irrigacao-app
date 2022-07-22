import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import Sidebar from ".";

test('if sidebar buttons are rendered', () => {
    render(
        <MemoryRouter>
            <Sidebar />
        </MemoryRouter>
    );

    expect(screen.getByText("Trajetória")).toBeInTheDocument();
    expect(screen.getByText("Controles")).toBeInTheDocument();
    expect(screen.getByText("Relatórios")).toBeInTheDocument();
})
