import React from 'react'
import Modal from 'react-bootstrap/Modal'
import Button from 'react-bootstrap/Button'
import Table from 'react-bootstrap/Table'
const BootstrapModal = ({ show, handleClose, event }) => {
   const title = event?.title || 'Modal Title'
   const id = event?.extendedProps.id || 'null'
   const updates = event?.extendedProps.updates

   const groupUpdates = updates?.reduce(function (r, a) {
      r[a.user_id] = r[a.user_id] || []
      r[a.user_id].push(a)
      return r
   }, Object.create(null))

   return (
      <Modal show={show} size='lg' onHide={() => handleClose(false)}>
         <Modal.Header closeButton>
            <Modal.Title>{title} ,</Modal.Title>
         </Modal.Header>
         <Modal.Header size='sm'>
            <div>What is your name?</div>
         </Modal.Header>
         <Modal.Header>
            <div>What is your age?</div>
         </Modal.Header>
         <Modal.Header>
            <div>What is your address?</div>
         </Modal.Header>

         <Modal.Body>
            <Table striped bordered hover>
               <thead>
                  <tr>
                     <td>#</td>
                     <td>Name</td>
                     <td>Role</td>
                     <td>Updates</td>
                  </tr>
               </thead>
               <tbody>
                  {!updates || updates.length < 1 ? (
                     <tr>
                        <td colSpan={4} className={'p-3 text-center'}>
                           No any updates
                        </td>
                     </tr>
                  ) : (
                     <>
                        {Object.keys(groupUpdates)?.map((update, idx) => {
                           return (
                              <tr key={idx}>
                                 <td>{idx + 1}</td>

                                 <td>{groupUpdates[update][0].user}</td>
                                 <td>{groupUpdates[update][0].role}</td>
                                 <td>
                                    {groupUpdates[update].map((data) => {
                                       return (
                                          <ul>
                                             <li>{data.comment}</li>
                                          </ul>
                                       )
                                    })}
                                 </td>
                                 {console.log(update)}
                              </tr>
                           )
                        })}
                        {/* {updates.map((update, idx) => {
                           return (
                              <tr>
                                 <td>{update?.user}</td>
                                 <td>{update?.role}</td>
                                 <td></td>
                              </tr>
                           )
                        })} */}
                     </>
                  )}
               </tbody>
            </Table>
         </Modal.Body>

         <Modal.Footer>
            <Button variant='secondary' onClick={() => handleClose(false)}>
               Close
            </Button>
            <Button variant='primary'>Save changes</Button>
         </Modal.Footer>
      </Modal>
   )
}

export default BootstrapModal
