import axios from "axios";
import dayjs from "dayjs";
import { jwtDecode } from "jwt-decode";
import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";


const baseURL = process.env.REACT_APP_BASE_URL

const useAxios = () =>{
    const {authTokens, setAuthTokens, setUser} = useContext(AuthContext)
    const axiosInstance = axios.create(
    {
        baseURL,
        headers:{Authorization:`Bearer ${authTokens?.access}`}
    })
    axiosInstance.interceptors.request.use(async config => {
        const user = jwtDecode(authTokens.access)
        const isTokenExpired = dayjs.unix(user.exp).diff(dayjs()) < 1;
        if(!isTokenExpired) return config
        const response = await axios.post(`${baseURL}/account/token/refresh/`,{
            refresh:authTokens.refresh
        })
        localStorage.setItem("authTokens", JSON.stringify(response.data))
        setAuthTokens(response.data)
        setUser(jwtDecode(response.data.access))
        config.headers.Authorization = `Bearer ${response.data.access}`
        return config
    })
    return axiosInstance


}

export default useAxios