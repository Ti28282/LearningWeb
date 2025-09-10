import React, {Suspense, useContext} from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { AuthContext } from "./components/AuthContext"

//<> Компоненты с отложенной загрузкой
const LoginPage = React.lazy(() => import("./auth/loginPage"));
const RegPage = React.lazy(() => import("./auth/regPage"));

const PrivateRoute = ({ children }) => {
    const {isAuthenticated} = useContext(AuthContext);
    return isAuthenticated ? children : <Navigate to="/login" />
}

function RoutePage() {
    return(
        <BrowserRouter>
            <Suspense fallback={<div className="loadingSpinner">Loading...</div>}>
                <Routes>
                    <Route path="/" element={
                        <PrivateRoute>
                        </PrivateRoute>
                    } />
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/register" element={<RegPage />} />
                </Routes>
            </Suspense>
        </BrowserRouter>
    )
}
export default RoutePage;