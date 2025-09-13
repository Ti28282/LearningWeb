import React, {Suspense, useContext} from "react";
import { BrowserRouter, Routes, Route, Navigate, useLocation } from "react-router-dom";
import { AuthContext } from "./components/AuthContext"
import App from "./main/app";
import NavigationLoader from "./components/loading/loader";

//todo Компоненты с отложенной загрузкой
//? React.lazy() загружает компоненты только когда они нужны
const LoginPage = React.lazy(() => import("./authorization/loginPage"));
const RegPage = React.lazy(() => import("./authorization/regPage"));
const Recovery = React.lazy(() => import("./passwordRecovery/recovery"));


//ye PrivateRoute проверяет авторизацию через AuthContext
const PrivateRoute = ({ children }) => {
    const {isAuthenticated} = useContext(AuthContext);
    //? Если пользователь не авторизован - перенаправляет на /login но если авторизован - показывает защищенные страницы
    return isAuthenticated ? children : <Navigate to="/login" />
}

const RecoveryGuard = ({children}) => {
    const location = useLocation()

    if(!location.state?.fromForgot) {  //? для проверки, как пользователь попал на страницу
        return <Navigate to="/login" replace />
    }

    return children  //? <Recovery /> рендерится только если пользователь пришёл «правильно».
}

function RoutePage() {
    return(
        <BrowserRouter>
            <Suspense fallback={<NavigationLoader />}>
                <Routes>
                    <Route
                        path="/"
                        element={
                            <PrivateRoute>
                                <App />
                            </PrivateRoute>
                        }
                    />
                    <Route 
                    path="/recovery" 
                    element={
                            <RecoveryGuard>
                                <Recovery />
                            </RecoveryGuard>
                        }
                    />
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/register" element={<RegPage />} />
                </Routes>
            </Suspense>
        </BrowserRouter>
    )
}
export default RoutePage;