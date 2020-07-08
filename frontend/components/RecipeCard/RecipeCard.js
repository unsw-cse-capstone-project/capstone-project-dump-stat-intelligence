import Link from "next/link";
import styles from "./RecipeCard.module.scss";

import Indicator from "./Indicator";

import { useDispatch } from "react-redux";
import { add_favourite } from "../../lib/redux/actions/authAction";

export default function RecipeCard(props) {
  const dispatch = useDispatch();
  function add() {
    dispatch(add_favourite({ name: props.title, id: props.id }));
  }
  return (
    <Link href={`/recipe/${props.id}`}>
      <div onClick={add} className={"card " + styles.recipe}>
        <div className="card-image">
          <figure className="image is-4by3">
            <img src={props.src} alt={props.title} />
          </figure>
        </div>
        <div className="card-content">
          <h4 className="title is-4">{props.title}</h4>
          <Indicator value="1">
            <li>Turkey</li>
            <li>Gravy</li>
            <li>Butter</li>
          </Indicator>
        </div>
      </div>
    </Link>
  );
}
