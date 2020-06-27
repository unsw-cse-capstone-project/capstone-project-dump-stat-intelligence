import style from "./EditDetails.module.scss";

import Modal from "../modal/Modal";

export default function EditDetails(props) {
    let form = <>
        EDIT THAT SHIIIIT
    </>
    return <Modal id={props.id} content={form}/>
}