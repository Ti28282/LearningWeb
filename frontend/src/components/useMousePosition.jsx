import React, {useEffect, useState} from "react";

function useMousePosition() {
const [mousePosition, setMousePosition] = useState({x: 0, y: 0});

        useEffect(() => {
            const mouseMoveHandler = (event) => {
                const {clientX, clientY} = event;
                setMousePosition({x: clientX, y: clientY});
            };
            document.addEventListener('mousemove', mouseMoveHandler);
            return () => {document.removeEventListener('mousemove', mouseMoveHandler);};
    }, []);
    return mousePosition
}
export default useMousePosition;