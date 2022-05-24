import React from 'react'
import Router from 'next/router'
import { Button } from 'react-bootstrap'
import useAuth from '../hooks/useAuth'
import Link from 'next/link'
const NavBar = () => {
   const me = useAuth()
   return (
      <div>
         {me && (
            <nav className='navbar navbar-expand-lg navbar-light bg-light'>
               <div className='container-fluid'>
                  <button
                     className='navbar-toggler'
                     type='button'
                     data-mdb-toggle='collapse'
                     data-mdb-target='#navbarSupportedContent'
                     aria-controls='navbarSupportedContent'
                     aria-expanded='false'
                     aria-label='Toggle navigation'
                  >
                     <i className=''></i>
                  </button>

                  <div className='collapse navbar-collapse' id='navbarSupportedContent'>
                     <a className='navbar-brand mt-2 mt-lg-0 text-decoration-none' href='#'>
                        {/* <img src='https://mdbcdn.b-cdn.net/img/logo/mdb-transaprent-noshadows.webp' height='15' alt='MDB Logo' loading='lazy' /> */}
                        {/* <h4>Synchron</h4> */}
                     </a>

                     <ul className='navbar-nav me-auto mb-2 mb-lg-0'>
                        <li className='nav-item'>
                           <Link href='/'>
                              <a className='nav-link'>Home</a>
                           </Link>
                        </li>
                        <li className='nav-item'>
                           <Link href='/dj/admin'>
                              <a className='nav-link'>Admin</a>
                           </Link>
                        </li>
                        <li className='nav-item'>
                           <Link href='/dj/swagger'>
                              <a className='nav-link'>Docs</a>
                           </Link>
                        </li>
                     </ul>
                  </div>

                  <div className='d-flex align-items-center'>
                     <div className='d-flex'>
                        <a
                           className=' d-flex align-items-center text-decoration-none'
                           href='#'
                           id='navbarDropdownMenuAvatar'
                           role='button'
                           data-mdb-toggle='dropdown'
                           aria-expanded='false'
                           onClick={async (e) => {
                              e.preventDefault()
                              const res = await fetch('http://127.0.0.1:4000/dj/accounts/logout', { method: 'GET', credentials: 'include' })
                              console.log(res)
                              Router.push(`/dj/accounts/login`)
                           }}
                        >
                           <Button type='submit'>logout</Button>
                        </a>
                        <a
                           className=' d-flex align-items-center text-decoration-none px-2'
                           href='#'
                           id='navbarDropdownMenuAvatar'
                           role='button'
                           data-mdb-toggle='dropdown'
                           aria-expanded='false'
                        >
                           {me.username} ({me.roles})
                        </a>
                     </div>
                  </div>
               </div>
            </nav>
         )}
      </div>
   )
}

export default NavBar
