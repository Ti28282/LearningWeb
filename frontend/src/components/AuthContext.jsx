import { createContext, useState } from "react";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [ isAuthenticated, setIsAunthenticated ] = useState(false);

    const login = () => setIsAunthenticated(true);
    const logout = () => setIsAunthenticated(false);

    return(
        <AuthContext.Provider value={{isAuthenticated, login, logout}}>
            {children}
        </AuthContext.Provider>
    )
}