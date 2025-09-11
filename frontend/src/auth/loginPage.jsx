import React, { useContext } from "react";
import './stylePage.scss'
import { Link } from "react-router-dom";
import { SquishyBox } from "../components/SquishyBox.jsx";
import { AuthContext } from "../components/AuthContext";

function LoginPage() {
    const { login } = useContext(AuthContext);

    const handleSubmit = (e) => {
        //<> Здесь должна быть логика проверки учетных данных
        //<> Если успешно, вызываем login()
        e.preventDefault();
        login()
    }

    return(
        <SquishyBox>
            <div className="login-container">
                <h2>Войти</h2>
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="email">Логин</label>
                        <input type="text" id="email" placeholder="Введите email или логин" required />
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">Пароль</label>
                        <input type="password" id="password" placeholder="Введите пароль" required />
                    </div>
                    <button type="submit">Войти</button>
                </form>
                <div className="footer"> Нет аккаунта?
                    <Link to="/register"> Зарегистрироваться</Link>
                </div>
            </div>
        </SquishyBox>
    )
}
export default LoginPage;