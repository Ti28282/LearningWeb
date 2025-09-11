import React, { useContext } from "react";
import './stylePage.scss'
import { Link } from "react-router-dom";
import {CSSTransition, TransitionGroup} from 'react-transition-group';
import { SquishyBox } from "../components/SquishyBox.jsx";
import { AuthContext } from "../components/AuthContext.jsx";

function LoginPage() {

    return(
        <div id="entryMainLogin">
            <div className="containerEntryDescription">
                <div className="loginCardOne">
                    <p className="entryText">Вход</p>
                    <div className="groupEmailPass">
                        <div className="groupForgot">
                            <input type="email" className="emailPlace" placeholder="Email"/>
                            <input type="password" className="passPlace" placeholder="Пароль"/>
                            <button className="forgotPass">ЗАБЫЛИ ПАРОЛЬ</button>
                        </div>
                        <button className="buttonRegistration"><Link className="registration" to="/register">РЕГИСТРАЦИЯ</Link></button>
                    </div>
                </div>
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