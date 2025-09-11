import React from "react";
import './stylePage.scss'
import { Link } from "react-router-dom";
import { SquishyBox } from "../components/SquishyBox.jsx";

function RegPage() {
    const handleSubmit = (e) => {
        e.preventDefault();
        //<> Здесь должна быть логика регистрации
        //<> После успешной регистрации можно перенаправить на /login
    }

    return(
        <SquishyBox>
            <div className="login-container">
                <h2>Регистрация</h2>
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="login">Логин</label>
                        <input type="text" id="login" placeholder="Введите email или логин" required />
                    </div>
                    <div className="form-group">
                        <label htmlFor="password">Пароль</label>
                        <input type="password" id="password" placeholder="Введите пароль" required />
                    </div>
                    <button type="submit">Зарегистрироваться</button>
                </form>
                <div className="footer"> Есть аккаунта?
                    <Link to="/login"> Войти</Link>
                </div>
            </div>
        </SquishyBox>
        
    )
}
export default RegPage;