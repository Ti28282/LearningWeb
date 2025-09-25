import React, { useState, useContext, useRef } from "react";
import './stylePage.scss'
import { Link, useNavigate } from "react-router-dom";
import { CSSTransition } from 'react-transition-group';
import { AuthContext } from "../components/AuthContext.jsx";
import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

function RegPage() {
    const [loginDataFilled, setLoginDataFilled] = useState("")
    const [emailDataFilled, setEmailDataFilled] = useState("")
    const [passDataFilled, setPassDataFilled] = useState("")   
    const [error, setError] = useState("");
    const nodeRef = useRef()

    const navigate = useNavigate() 
    const {login} = useContext(AuthContext);

    const stateLoginFilled = (e) => {
        setLoginDataFilled(e.target.value)
    }
    const stateEmailFilled = (e) => {
        setEmailDataFilled(e.target.value)
    }
    const statePassFilled = (e) => {
        setPassDataFilled(e.target.value)
    }

    const areFieldsFilled = emailDataFilled.trim() !== "" && passDataFilled.trim() !== "" && loginDataFilled.trim() !== "";

    //todo Логика Регистрации

    const handleRegister = async (e) => {
        e.preventDefault()

        if(!areFieldsFilled) return

        setError("")

        try {
            const response = await axios.post(`${API_URL}/api/v0/register`, 
                {
                    email: emailDataFilled,
                    password: passDataFilled,
                    username: loginDataFilled,
                }, {
            }); console.log(response.data)

            if(response.status >= 200 && response.status <= 300) {
                const token = response.data.access_token
                if(token) {
                    localStorage.setItem('authToken' ,token)
                }
                
                login()

                navigate('/')
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
        <div id="entryMainReg">
            <div className="containerRegDescription">
                <CSSTransition
                    in={true}
                    appear={true}
                    timeout={500}
                    classNames="pageTransition"
                    nodeRef={nodeRef}
                >
                    <div className="regCardOne" ref={nodeRef}>
                        <p className="regText">Регистрация</p>
                        <div className="groupEmailPass">
                            <div className="groupForgot">
                                <input type="text" 
                                className="loginPlace" 
                                placeholder="Логин" 
                                onChange={stateLoginFilled}
                                />
                                <input type="email" 
                                className="emailPlace" 
                                placeholder="Email" 
                                onChange={stateEmailFilled}
                                />
                                <input type="password" 
                                className="passPlace" 
                                placeholder="Пароль" 
                                onChange={statePassFilled}
                                />
                            </div>
                            <button className={`buttonEntry ${areFieldsFilled ? 'hidden' : ''}`}><Link className="entry" to="/login">УЖЕ ЕСТЬ АККАУНТ</Link></button>
                            <button className={`buttonRegister ${areFieldsFilled ? 'visible' : ''}`} onClick={handleRegister}>ЗАРЕГИСТРИРОВАТЬСЯ</button>
                        </div>
                    </div>    
                </CSSTransition>
                <div className="regCardTwo">
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
export default RegPage;