import React, { FC } from 'react';
import { Link } from 'react-router-dom';
import { Breadcrumbs } from '../../../api/typings/document';
import { ReactComponent as navigation } from '@epam/assets/icons/common/navigation-chevron-right-12.svg';
import { IconButton } from '@epam/loveship';
import styles from './breadcrumb-navigation.module.scss';

type BreadcrumbNavigationProps = {
    breadcrumbs: Breadcrumbs[];
};

export const BreadcrumbNavigation: FC<BreadcrumbNavigationProps> = ({ breadcrumbs }) => {
    return (
        <div className="flex">
            {breadcrumbs.map(({ name, url }, index) => (
                <div key={name}>
                    {breadcrumbs.length > 1 && breadcrumbs.length - 1 !== index && url ? (
                        <div className="flex flex-center">
                            <Link to={url}>
                                <div className={`${styles.title} ${styles['title-active']}`}>
                                    {name}
                                </div>
                            </Link>
                            <div className={styles.divider}>
                                <IconButton icon={navigation} />
                            </div>
                        </div>
                    ) : (
                        <div className={`${styles.title} ${styles['title-passive']}`}>{name}</div>
                    )}
                </div>
            ))}
        </div>
    );
};
