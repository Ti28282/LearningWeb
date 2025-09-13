import React, { useState, useContext } from "react";
import './stylePage.scss'
import { Link, useNavigate } from "react-router-dom";
import { CSSTransition } from 'react-transition-group';
import { AuthContext } from "../components/AuthContext.jsx";
import axios from "axios";

function LoginPage() {
    const [emailDataFilled, setEmailDataFilled] = useState("")
    const [passDataFilled, setPassDataFilled] = useState("")
    const [error, setError] = useState("")


    //! КОНТЕКСТ АУТЕНТИФИКАЦИИ И НАВИГАЦИЯ
    
    const {login} = useContext(AuthContext); //? Функция login из контекста для обновления состояния авторизации
    const navigate = useNavigate()  //? Хук для программной навигации между страницами

    //! ОБРАБОТЧИКИ ИЗМЕНЕНИЯ ПОЛЕЙ ВВОДА
    const stateEmailFilled = (e) => {
        setEmailDataFilled(e.target.value)
        setError("")
    }
    const statePassFilled = (e) => {
        setPassDataFilled(e.target.value)
        setError("")
    }

    //ye Проверка заполнены ли оба поля ввода
    const areFieldsFilled = emailDataFilled.trim() !== "" && passDataFilled.trim() !== "";

    //todo Логика авторизации
    
    const handleLogin = async (e) => {
        e.preventDefault()  //? Предотвращаем стандартное поведение формы

        if(!areFieldsFilled) return //? Если поля не заполнены выходим

        setError("") //? Сброс ошибок

        try{
            const response = await axios.post('http://93.157.248.178:5010/api/v0/user/login', {
                email: emailDataFilled,
                password: passDataFilled,
            }, {
                headers: {
                    'Content-Type': 'aplication/json' //? Указываем тип данных
                }
            })

            if(response.status == 200) {
                //? Сохраняем токен в localStorage для последующих запросов
                const token = response.data.access_token;
                if(token) {
                    localStorage.setItem('authToken', token)
                }

                login() //? Обновляем глобальное состояние аутентификации (isAuthenticated = true)

                navigate('/') //? Перенаправление пользователя на глаавную страницу
            }

        } catch (error) {
            console.error("Ошибка автороизации", error)

            if(error.response) {
                switch(error.response.status) {
                    case 401: 
                        setError("Неверный email или пароль")
                        break
                    case 404:
                        setError("Пользователь не найден")
                        break
                    case 500:
                        setError("Ошибка сервера. Попробуйте позже")
                        break
                    default:
                        setError("Произошла ошибка при авторизации")
                }
            } else if (error.request) {
                setError("Нет ответа от сервера. Проверьте подключение")
            } else {
                setError("Произошла непредвиденная ошибка")
            }
        }
    }
    return(
        <div id="entryMainLogin">
            <div className="containerEntryDescription">
                <CSSTransition
                    in={true}
                    appear={true}
                    timeout={500}
                    classNames="pageTransition"
                >
                    <div className="loginCardOne">
                        <p className="entryText">Вход</p>
                        <div className="groupEmailPass">
                            <div className="groupForgot">
                                <input 
                                type="email" 
                                className="emailPlace" 
                                placeholder="Email" 
                                onChange={stateEmailFilled}
                                />
                                <input 
                                type="password" 
                                className="passPlace" 
                                placeholder="Пароль" 
                                onChange={statePassFilled}
                                />
                                <button className="forgotPass" onClick={() => navigate("/recovery", { state: { fromForgot: true } })}>ЗАБЫЛИ ПАРОЛЬ</button>
                            </div>
                            <button className={`buttonRegistration ${areFieldsFilled ? 'hidden' : ''}`}><Link className="registration" to="/register">РЕГИСТРАЦИЯ</Link></button>
                            <button className={`buttonLog ${areFieldsFilled ? 'visible' : ''}`}
                                onClick={handleLogin}
                                >
                                    ВОЙТИ
                                </button>
                        </div>
                    </div>
                </CSSTransition>
                <div className="loginCardTwo">
                    <div className="textDescription">
                        <h1 className="textWelcome">Добро пожаловать в Name!</h1>
                        <p className="text">С точки зpения банальной эpyдиции каждый индивидyyм, кpитически мотивиpyющий абстpакцию, не может игноpиpовать кpитеpии yтопического сyбьективизма.</p>
                        <p className="text">С точки зpения банальной эpyдиции каждый индивидyyм, кpитически мотивиpyющий абстpакцию, не может игноpиpовать кpитеpии yтопического сyбьективизма.</p>
                        <p className="text">С точки зpения банальной эpyдиции каждый индивидyyм, кpитически мотивиpyющий абстpакцию, не может игноpиpовать кpитеpии yтопического сyбьективизма.</p>
                        <p className="text">С точки зpения банальной эpyдиции каждый индивидyyм, кpитически мотивиpyющий абстpакцию, не может игноpиpовать кpитеpии yтопического сyбьективизма.</p>
                        <p className="text">С точки зpения банальной эpyдиции каждый индивидyyм, кpитически мотивиpyющий абстpакцию, не может игноpиpовать кpитеpии yтопического сyбьективизма.</p>
                    </div>
                </div>
            </div>
        </div>
    )
}
export default LoginPage;