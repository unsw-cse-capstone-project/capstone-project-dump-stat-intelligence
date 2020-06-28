import styles from "./Pantry.module.scss";

import React from "react";

import Pantry from "./Pantry";

export default class Indicator extends React.Component {
  constructor(props) {
    super(props);
    this.state = { open: false };
  }
  render() {
    return (
      <>
        <div
          onClick={() => this.setState({ open: !this.state.open })}
          className={styles.pantryButton}
        >
          <img src="/fridge.svg" />
        </div>
        {this.state.open ? <Pantry /> : null}
      </>
    );
  }
}
