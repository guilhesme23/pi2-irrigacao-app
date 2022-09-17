import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import ControlPanelHeader from ".";

test('if control panel header text is rendered', () => {
    render(
        <MemoryRouter>
            <ControlPanelHeader />
        </MemoryRouter>
    )

    expect(screen.getByText('Painel de controle')).toBeInTheDocument()
})

test('if auxiliary data is rendered', () => {
    render(
        <MemoryRouter>
            <ControlPanelHeader />
        </MemoryRouter>
    )

    expect(screen.getByText('Temperatura: 23 °C')).toBeInTheDocument()
    expect(screen.getByText('Umidade: 45 %')).toBeInTheDocument()
})