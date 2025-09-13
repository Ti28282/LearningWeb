import "./styleLoad.scss";

const NavigationLoader = () => {

    return (
        <div className="loader">
            <div className="loaderBackground">
                <div className="loaderContent">
                    <div className="loaderSpinner"></div>
                </div>
            </div>
        </div>
    );
};

export default NavigationLoader;
