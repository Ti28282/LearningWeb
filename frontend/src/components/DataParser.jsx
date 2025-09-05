import React, {useState, useEffect} from "react";
import axios from "axios"

const DataParser = () => {
    const [weather, setWeather] = useState(null)
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState(null)

    const API_KEY = "50184243a12e0e6ae507cdb80aa7e200";
    const lat = 55.7887;
    const lon = 49.1221;
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric&lang=ru`;
    
    const fetchWeather = async () => {
        try{
            const response = await axios.get(url);
            setWeather(response.data)
        } catch (err) {
            setError('Ошибка загрузки погоды')
            console.error(err)
        } finally {
            setLoading(false)
        }
    }
    useEffect(() => {
        fetchWeather()
        const intervalWindow =  window.innerWidth < 768 ? 300000 : 60000
        const interval = setInterval(fetchWeather, intervalWindow)
        return () => clearInterval(interval)
    }, [])

    if(loading) return <div>Загрузка...</div>
    if(error) return <div>{error}</div>

    return {weather}
}
export default DataParser;