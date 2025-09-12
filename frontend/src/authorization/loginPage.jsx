import React, { useState, useContext } from "react";
import './stylePage.scss'
import { Link } from "react-router-dom";
import {CSSTransition} from 'react-transition-group';
import { AuthContext } from "../components/AuthContext.jsx";

function LoginPage() {
    const [emailDataFilled, setEmailDataFilled] = useState("")
    const [passDataFilled, setPassDataFilled] = useState("")

    const stateEmailFilled = (e) => {
        setEmailDataFilled(e.target.value)
    }
    const statePassFilled = (e) => {
        setPassDataFilled(e.target.value)
    }

    const areFieldsFilled = emailDataFilled.trim() !== "" && passDataFilled.trim() !== "";

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
                                <input type="email" className="emailPlace" placeholder="Email" onChange={stateEmailFilled}/>
                                <input type="password" className="passPlace" placeholder="Пароль" onChange={statePassFilled}/>
                                <button className="forgotPass">ЗАБЫЛИ ПАРОЛЬ</button>
                            </div>
                            <button className={`buttonRegistration ${areFieldsFilled ? 'hidden' : ''}`}><Link className="registration" to="/register">РЕГИСТРАЦИЯ</Link></button>
                            <button className={`buttonLog ${areFieldsFilled ? 'visible' : ''}`}>ВОЙТИ</button>
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