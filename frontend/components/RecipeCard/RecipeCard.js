import Link from "next/link";
import styles from "./RecipeCard.module.scss";

import Indicator from "./Indicator";

import { useDispatch } from "react-redux";
import { add_favourite } from "../../lib/redux/actions/authAction";

export default function RecipeCard(props) {
  const dispatch = useDispatch();
  function add() {
    dispatch(add_favourite({ name: props.recipe.name, id: props.recipe.id }));
  }
  return (
    <Link href={`/recipe/[recipeId]`} as={`/recipe/${props.recipe.id}`}>
      <div onClick={add} className={"card " + styles.recipe}>
        <div className="card-image">
          <figure className="image is-4by3">
            <img src={props.src} alt={props.recipe.name} />
          </figure>
        </div>
        <div className="card-content">
          <h4 className="title is-5" style={{ textAlign: "center" }}>
            {props.recipe.name}
          </h4>
          <p>
            {props.recipe.author.username} | {props.recipe.cook_time}
          </p>
          <Indicator value={props.recipe.ingredients.length}>
            <ul>
              {props.recipe.ingredients.forEach((ingredient, idx) => (
                <li key={idx}>{ingredient}</li>
              ))}
            </ul>
          </Indicator>
        </div>
      </div>
    </Link>
  );
}
