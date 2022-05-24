import React, { useEffect, useState } from 'react'
import Router from 'next/router'

const useAuth = () => {
   const [resData, setResData] = useState(null)
   const [resStatus, setResStatus] = useState(null)

   useEffect(() => {
      const { pathname } = Router
      const fetchData = async () => {
         const res = await fetch('http://127.0.0.1:4000/dj/api/users/me', { method: 'GET', credentials: 'include' })
         const data = await res.json()
         setResStatus(res.status)
         setResData(data)
         console.log(data)
      }
      fetchData()
   }, [])
   useEffect(() => {
      if (resStatus === 403) return Router.push(`/dj/accounts/login`)
   }, [resStatus])

   return resData
}

export default useAuth
