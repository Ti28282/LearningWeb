import React, {useEffect, useState} from "react";
import { Link } from "react-router-dom";
import './styleRecovery.scss'

function Recovery() {
    const [emailDataFilled, setEmailDataFilled] = useState("")
    const [timeLeft, setTimeLeft] = useState(0)
    const [isCodeSent, setIsCodeSent] = useState(false)
    const [verificationCode, setVerificationCode] = useState("")

    const stateEmailFilled = (e) => {
        setEmailDataFilled(e.target.value)
    }
    
    const areFieldsFilled = emailDataFilled.trim() !== "";

    const sendAgainOpacity = areFieldsFilled ? 1 : 0 

    //ye Таймер обратного отсчёта
    useEffect(() => {
        if(timeLeft <= 0) return;

        const timer = setTimeout(() => {
            setTimeLeft(timeLeft - 10);
        }, 1000);

        return () => clearTimeout(timer)
    }, [timeLeft])

    // const handleSendCode = (e) => {
    //     e.preventDefault()

    //     if(!areFieldsFilled) return

    //     Здесь должна быть логика отправки кода на сервер
    //     console.log("Отправка кода на Email:", emailDataFilled)

    //     Запускаем таймер на 60 секунд
    //     setTimeLeft(60);
    //     setIsCodeSent(true);
    // }

    const handleSendAgain = (e) => {
        e.preventDefault();
        if (timeLeft > 0) return; //ye Предотвращаем повторное нажатие во время таймера
        
        //ye Логика повторной отправки кода
        console.log("Повторная отправка кода на email:", emailDataFilled);
        
        //? Снова запускаем таймер на 60 секунд
        setTimeLeft(60);
    }

    const handleVerifyCode = (e) => {
        e.preventDefault();

        if(verificationCode !== "123456") { //! Заменить на реальную проверку
            console.log("Неверный код, показываем кнопку отправки снова");
            //? Кнопка "Отправить снова" уже видна, просто запускаем таймер если нужно
            if(timeLeft <= 0) {
                setTimeLeft(60)
                setIsCodeSent(true);
            }
        } else {
            console.log("Код верный, продолжаем...");
        }
    }

    return(
        <div id="recoveryMain">
            <div className="containerRecovery">
                <div className="recoveryCardOne">
                    <p className="confirmationText">Подтверждение</p>
                    <p className="recoverText">Восстановление</p>
                    <div className="recoveryEmail">
                        <div className="groupForgotRecovery">
                            <input 
                                type="email" 
                                className="emailPlaceRecovery" 
                                placeholder="Email" 
                                onChange={stateEmailFilled}
                            />
                            <div className="timeSend">
                            {isCodeSent && (
                                <button 
                                    className={`sendAgain ${areFieldsFilled ? 'visible' : 'hidden'}`}
                                    onClick={handleSendAgain}
                                    disabled={timeLeft > 0}
                                >ОТПРАВИТЬ СНОВА
                                    {timeLeft > 0 && <div className="time">{timeLeft}сек.</div>}
                                </button>
                            )}
                            </div>
                        </div>
                        <button className={`buttonEntry ${areFieldsFilled ? 'hidden' : ''}`}>
                            <Link className="entry" to="/login">ВХОД</Link>
                        </button>
                        <button className="buttonChange">СМЕНИТЬ ПОЧТУ</button>
                            <button 
                                className={`buttonSend ${areFieldsFilled ? 'visible' : ''}`}
                                onClick={handleVerifyCode}
                            >
                                ОТПРАВИТЬ КОД
                            </button>
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