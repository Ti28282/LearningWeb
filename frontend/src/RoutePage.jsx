import React, {Suspense, useContext} from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { AuthContext } from "./components/AuthContext"
import App from "./main/app";

//<> Компоненты с отложенной загрузкой
const LoginPage = React.lazy(() => import("./authorization/loginPage"));
const RegPage = React.lazy(() => import("./authorization/regPage"));
const Recovery = React.lazy(() => import("./passwordRecovery/recovery"));

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
                            <App />
                        </PrivateRoute>
                    } />
                    <Route path="/recovery" element={<Recovery />} />
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/register" element={<RegPage />} />
                </Routes>
            </Suspense>
        </BrowserRouter>
    )
}
export default RoutePage;