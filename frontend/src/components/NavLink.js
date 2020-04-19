import React from "react";
import PropTypes from "prop-types";
import { NavLink as Link } from "react-router-dom";
import styled from "styled-components";
import { Box } from "rebass";

const StyledLink = styled(Link)`
  font-size: ${(props) => props.theme.fontSizes.medium};
  border-bottom: 3px solid transparent;
  line-height: ${(props) => props.theme.fontSizes.medium};
  padding-bottom: 10px;
  text-decoration: none;
  &.active {
    border-color: ${(props) => props.theme.colors.yellow};
  }
`;

function NavLink({ title, href, ...rest }) {
  return (
    <Box mb="30px" {...rest}>
      <StyledLink to={href} activeClassName="active" {...rest}>
        {title}
      </StyledLink>
    </Box>
  );
}

NavLink.propTypes = {
  title: PropTypes.string.isRequired,
  href: PropTypes.string.isRequired,
};

export default NavLink;
