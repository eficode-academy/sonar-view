import React from "react";
import PropTypes from "prop-types";
import { NavLink } from "react-router-dom";
import styled from "styled-components";
import { Box } from "rebass";

const StyledLink = styled(NavLink)`
  font-size: ${(props) => props.theme.fontSizes.medium};
  border-bottom: 3px solid transparent;
  line-height: ${(props) => props.theme.fontSizes.medium};
  padding-bottom: 10px;

  &.active {
    border-color: ${(props) => props.theme.colors.yellow};
  }
`;

function Link({ title, href, exact }) {
  return (
    <Box mb="30px">
      <StyledLink to={href} exact={exact} activeClassName="active">
        {title}
      </StyledLink>
    </Box>
  );
}

Link.defaultProps = {
  exact: false,
};

Link.propTypes = {
  title: PropTypes.string.isRequired,
  href: PropTypes.string.isRequired,
  exact: PropTypes.bool,
};

export default Link;
