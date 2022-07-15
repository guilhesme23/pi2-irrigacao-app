import { render, screen } from "@testing-library/react";
import Sidebar from ".";

test('if sidebar buttons are rendered', () => {
    render(<Sidebar />);
    expect(screen.getByText("Trajetória")).toBeInTheDocument();
    expect(screen.getByText("Relatórios")).toBeInTheDocument();
    expect(screen.getByText("Sensores")).toBeInTheDocument();
})
