
import { useDispatch } from "react-redux";
import Check from "../Pantry/Check";


export default function DropItem(props) {
    const dispatch = useDispatch();
    function deal() {
        if (props.is_checked) {
            dispatch(props.remove(props.name, props.category));
        } else {
            dispatch(props.add(props.name, props.category));
        }
    }
    return <a onClick={deal} className="dropdown-item">
        <span>{props.name}</span>
        {props.is_checked ? <Check/> : ""}
    </a>
}