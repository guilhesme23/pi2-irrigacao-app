import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import SensorStatusBox from ".";


test('if sensor status is rendered', async () => {
    render(
        <MemoryRouter>
            <SensorStatusBox />
        </MemoryRouter>
    );

    expect(screen.getByText("Data/Hora")).toBeInTheDocument();
    expect(screen.getByText("Atividade")).toBeInTheDocument();

})
