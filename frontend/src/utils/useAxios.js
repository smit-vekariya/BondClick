import axios from "axios";
import dayjs from "dayjs";
import { jwtDecode } from "jwt-decode";
import { useContext } from "react";
import { AuthContext } from "../context/AuthContext";


const baseURL = process.env.REACT_APP_BASE_URL

const useAxios = () =>{
    const {authTokens, setAuthTokens, setUser, setLoading} = useContext(AuthContext)
    const axiosInstance = axios.create(
    {
        baseURL,
        headers:{Authorization:`Bearer ${authTokens?.access}`}
    })
    axiosInstance.interceptors.request.use(async config => {
        setLoading(true)
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
    axiosInstance.interceptors.response.use(function (response) {
        setLoading(false)
    return response;
    }, function (error) {
        return Promise.reject(error);
    });
    return axiosInstance


}

export default useAxios




// import axios from "axios";
// import dayjs from "dayjs";
// import { jwtDecode } from "jwt-decode";

// //this page is not in use now

// const baseURL = 'http://127.0.0.1:8000'

// let authTokens =  localStorage.getItem("authTokens") ? JSON.parse(localStorage.getItem("authTokens")):null

// const axiosInstance = axios.create(
//     {
//         baseURL,
//         headers:{Authorization:`Bearer ${authTokens?.access}`}
//     }
// )

// axiosInstance.interceptors.request.use(async config => {
//     if(!authTokens){
//         let authTokens =  localStorage.getItem("authTokens") ? JSON.parse(localStorage.getItem("authTokens")):null
//         config.headers.Authorization = `Bearer ${authTokens?.access}`
//     }

//     const user = jwtDecode(authTokens.access)
//     const isTokenExpired = dayjs.unix(user.exp).diff(dayjs()) < 1;
//     if(!isTokenExpired) return config

//     const response = await axios.post(`${baseURL}/account/token/refresh/`,{
//         refresh:authTokens.refresh
//     })
//     localStorage.setItem("authTokens", JSON.stringify(response.data))
//     localStorage.setItem("access", response.data["access"])
//     config.headers.Authorization = `Bearer ${authTokens?.access}`
//     return config
//   })

// export default axiosInstance