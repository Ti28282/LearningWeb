import React, {useState} from "react";
import "./App.scss";
import SystemInfo from "./systemInfo.jsx";
import { Outlet } from "react-router";
import DataParser from "../components/DataParser.jsx";

function App() {
    const [isSidebarOpen, setIsSidebarOpen] = useState(false);
    const {weather} = DataParser();
    const toggleSidebar = () => {
        setIsSidebarOpen(!isSidebarOpen)
    }

    const capitalize = (str) => {
        return str.charAt(0).toUpperCase() + str.slice(1)
    }

    return (
      <div className="app">
        <button className={`mobile-menu-toggle ${isSidebarOpen ? 'active' : ''}`}
          onClick={toggleSidebar}
        >
          <img src="three-line-horizontal-svgrepo-com.svg" alt="mobile menu" />
        </button>
        {/* Навигационная панель */}
        <nav className={`sidebar ${isSidebarOpen ? 'active' : ''}`}>
          <ul className="menu">
            <li className="active">📊 Главная</li>
            <li>💻 Устройства</li>
            <li>⚙️ Настройки</li>
            <li>📢 Уведомления</li>
            <li>❓ Помощь</li>
          </ul>
          <div className="user-info">
            <div className="avatar">JD</div>
            <span className="email">John Doe</span>
          </div>
        </nav>
        <SystemInfo isSidebarOpen={isSidebarOpen}/>
        {/* Сайдбар справа (погода) */}
        <aside className="sidebar-right">
          <div className="weather-card">
            {weather && weather.weather ? (
                <>
                    <img className="weather-icon" src={`https://openweathermap.org/img/wn/${weather.weather[0].icon}@4x.png`}/>
                    <div>
                        <h2 className="location">Погода в {weather?.name}</h2>
                        <div className="temperature">{weather.main.temp.toFixed(0)}°C</div>
                        <div className="weather-details">
                            <p className="weather-feels">Ощущается как: {weather.main.feels_like.toFixed(0)}°C</p>
                            <p className="weather-speed">Ветер: {weather.wind.speed} м/с</p>
                            <p className="weather-description">Облачность: {capitalize(weather.weather[0].description)}</p>
                        </div>
                    </div>
                </>
            ) : (
                <div>Данные о погоде не доступны</div>
            )}
          </div>
        </aside>
        {/* //? Контейнер для вложенных маршрутов */}
        <Outlet />
      </div>
    );
}

export default App;