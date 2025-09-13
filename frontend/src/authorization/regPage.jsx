import React, { useState } from "react";
import './stylePage.scss'
import { Link } from "react-router-dom";
import {CSSTransition} from 'react-transition-group';
import { useNavigate } from "react-router-dom";

function RegPage() {
    const [loginDataFilled, setLoginDataFilled] = useState("")
    const [emailDataFilled, setEmailDataFilled] = useState("")
    const [passDataFilled, setPassDataFilled] = useState("")

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

    return(
        <div id="entryMainReg">
            <div className="containerRegDescription">
                <CSSTransition
                    in={true}
                    appear={true}
                    timeout={500}
                    classNames="pageTransition"
                >
                    <div className="regCardOne">
                        <p className="regText">Регистрация</p>
                        <div className="groupEmailPass">
                            <div className="groupForgot">
                                <input type="text" className="loginPlace" placeholder="Логин" onChange={stateLoginFilled}/>
                                <input type="email" className="emailPlace" placeholder="Email" onChange={stateEmailFilled}/>
                                <input type="password" className="passPlace" placeholder="Пароль" onChange={statePassFilled}/>
                            </div>
                            <button className={`buttonEntry ${areFieldsFilled ? 'hidden' : ''}`}><Link className="entry" to="/login">УЖЕ ЕСТЬ АККАУНТ</Link></button>
                            <button className={`buttonRegister ${areFieldsFilled ? 'visible' : ''}`}>ЗАРЕГИСТРИРОВАТЬСЯ</button>
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