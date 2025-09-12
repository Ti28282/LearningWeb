import React, {useState} from "react";
import { Link } from "react-router-dom";
import './styleRecovery.scss'

function Recovery() {
    const [emailDataFilled, setEmailDataFilled] = useState("")

    const stateEmailFilled = (e) => {
        setEmailDataFilled(e.target.value)
    }
    
    const areFieldsFilled = emailDataFilled.trim() !== "";

    return(
        <div id="recoveryMain">
            <div className="containerRecovery">
                <div className="recoveryCardOne">
                    <p className="confirmationText">Подтверждение</p>
                    <p className="recoverText">Восстановление</p>
                    <div className="recoveryEmail">
                        <div className="groupForgotRecovery">
                            <input type="email" className="emailPlaceRecovery" placeholder="Email" onChange={stateEmailFilled}/>
                            <div className="timeSend">
                                <input type="text" className="sendAgain" placeholder="ОТПРАВИТЬ СНОВА"/><div className="time">60сек.</div>
                            </div>
                        </div>
                        <button className={`buttonEntry ${areFieldsFilled ? 'hidden' : ''}`}><Link className="entry" to="/login">ВХОД</Link></button>
                        <button className="buttonChange">СМЕНИТЬ ПОЧТУ</button>
                        <button className={`buttonSend ${areFieldsFilled ? 'visible' : ''}`}>ОТПРАВИТЬ КОД</button>
                    </div>
                </div>
                <div className="recoveryCardTwo">
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

export default Recovery;