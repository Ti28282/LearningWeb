import React from "react";
import './stylePage.scss'
import { Link } from "react-router-dom";
import {CSSTransition, TransitionGroup} from 'react-transition-group';
import { SquishyBox } from "../components/squishyBox.jsx";

function RegPage() {

    return(
        <div id="entryMainReg">
            <div className="containerRegDescription">
                <div className="regCardOne">
                    <p className="regText">Регистрация</p>
                    <div className="groupEmailPass">
                        <div className="groupForgot">
                            <input type="text" className="loginPlace" placeholder="Логин"/>
                            <input type="email" className="emailPlace" placeholder="Email"/>
                            <input type="password" className="passPlace" placeholder="Пароль"/>
                        </div>
                        <button className="buttonEntry"><Link className="entry" to="/login">УЖЕ ЕСТЬ АККАУНТ</Link></button>
                    </div>
                </div>
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