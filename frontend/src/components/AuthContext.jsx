import { createContext, useState } from "react";

//ye Cам контекст для распространения данных
export const AuthContext = createContext();

//! Компонент-обертка, который:
//? Хранит состояние авторизации
//? Предоставляет функции login/logout
//? Оборачивает дочерние компоненты для доступа к контексту

export const AuthProvider = ({ children }) => {
    const [ isAuthenticated, setIsAunthenticated ] = useState(false);
    //ye вход и выход
    const login = () => setIsAunthenticated(true);
    const logout = () => setIsAunthenticated(false);

    return(
        <AuthContext.Provider value={{isAuthenticated, login, logout}}>
            {children}
        </AuthContext.Provider>
    )
}