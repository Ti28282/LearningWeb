import React, { useRef } from "react";
import useMousePosition from "./useMousePosition";
import '../auth/stylePage.scss'

export const SquishyBox = ({children}) => {
    const boxRef = useRef(null);
        const { x: mouseX, y: mouseY } = useMousePosition();
    
         const handleMouseMove = () => {
            if (!boxRef.current) return;
    
            const box = boxRef.current;
            const { left, top, width, height } = box.getBoundingClientRect();
            const centerX = left + width / 2;
            const centerY = top + height / 2;
    
            // Считаем смещение курсора относительно центра блока
            const deltaX = (mouseX - centerX) / (width / 2);  // от -1 до 1
            const deltaY = (mouseY - centerY) / (height / 2); // от -1 до 1
    
            // Применяем деформацию
            const skewX = deltaY * 5;  // Наклон по X зависит от Y (и наоборот)
            const skewY = -deltaX * 5;
            const rotateX = deltaY * -1.5;
            const rotateY = deltaX * 1.5;
    
            box.style.transform = `
                perspective(500px)
                scale(1.03)
                rotateX(${rotateX}deg)
                rotateY(${rotateY}deg)
                
            `;
        }
        const handleMouseLeave = () => {
            if (boxRef.current) {
                boxRef.current.style.transform = 'none';
            }
        }
    return (
        <div id="squishy"
            ref={boxRef}
            onMouseMove={handleMouseMove}
            onMouseLeave={handleMouseLeave}
        >
            {children}
        </div>
    )
}