import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import AreaDisplay from ".";


test('if area display text is rendered', () => {
    render(
        <MemoryRouter>
            <AreaDisplay />
        </MemoryRouter>
    );

    expect(screen.getByText("Área de alcance do aspersor = 3m")).toBeInTheDocument();
})
