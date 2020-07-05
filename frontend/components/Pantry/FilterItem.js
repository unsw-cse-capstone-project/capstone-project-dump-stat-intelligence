import styles from "./Filter.module.scss";
import { useDispatch } from "react-redux";
import { filter_update } from "../../lib/redux/actions/exploreAction";
import Check from "./Check";

export default function FilterItem(props) {
    const dispatch = useDispatch();
    

    return <a onClick={() => dispatch(filter_update(props.category, props.name, !props.is_checked))} key={props.idx} className="dropdown-item">
        <span>{props.name}</span>
        {props.is_checked ? <Check/> : ""}
    </a>
}