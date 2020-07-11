
import { useDispatch } from "react-redux";
import Check from "../Pantry/Check";


export default function DropItem(props) {
    const dispatch = useDispatch();

    return <a onClick={() => dispatch(props.func(props.name))} className="dropdown-item">
        <span>{props.name}</span>
        {props.is_checked ? <Check/> : ""}
    </a>
}