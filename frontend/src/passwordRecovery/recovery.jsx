

function Recovery() {

    return(
        <div id="recoveryMain">
            <div className="containerRecovery">
                <div className="recoveryCardOne">
                    <p className="entryText">Восстановление</p>
                    <div className="recoveryEmail">
                        <div className="groupForgot">
                            <input type="email" className="emailPlace" placeholder="Email"/>
                            <input type="text" placeholder="ОТПРАВИТЬ СНОВА"/><div>60сек</div>
                        </div>
                        <button className="buttonEntry"><Link className="entry" to="/login">ВХОД</Link></button>
                        <button>СМЕНИТЬ ПОЧТУ</button>
                        <button>ОТПРАВИТЬ КОД</button>
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